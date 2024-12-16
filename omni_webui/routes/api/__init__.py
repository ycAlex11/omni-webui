from fastapi import APIRouter
from sqlmodel import col, func, select

from ... import __version__
from ...config import get_env, get_settings
from ...deps import AsyncSessionDepends
from ...models.config import get_config
from ...models.user import User, UserDepends
from .v1 import router as v1_router

router = APIRouter()
router.include_router(v1_router, prefix="/v1")


@router.get("/config")
async def retrieve_config(
    *,
    user: UserDepends,
    session: AsyncSessionDepends,
):
    env = get_env()
    webui = get_settings()
    config = await get_config()

    onboarding = False
    if user is None:
        user_count = (await session.exec(select(func.count(col(User.id))))).one()
        onboarding = user_count == 0

    return {
        **({"onboarding": True} if onboarding else {}),
        "status": True,
        "name": webui.name,
        "version": __version__,
        "default_locale": config.ui.default_locale,
        "oauth": {
            "providers": {
                name: provider.get("name", name)
                for name, provider in config.oauth.providers.items()
            }
        },
        "features": {
            "auth": webui.auth,
            "auth_trusted_header": bool(webui.auth_trusted_email_header),
            "enable_ldap": config.ldap.enable,
            "enable_api_key": config.auth.api_key.enable,
            "enable_signup": config.ui.enable_signup,
            "enable_login_form": config.ui.ENABLE_LOGIN_FORM,
            **(
                {
                    "enable_web_search": config.rag.web.search.enable,
                    "enable_image_generation": config.image_generation.enable,
                    "enable_community_sharing": config.ui.enable_community_sharing,
                    "enable_message_rating": config.ui.enable_message_rating,
                    "enable_admin_export": env.enable_admin_export,
                    "enable_admin_chat_access": env.enable_admin_chat_access,
                }
                if user is not None
                else {}
            ),
        },
        **(
            {
                "default_models": config.ui.default_models,
                "default_prompt_suggestions": config.ui.prompt_suggestions,
                "audio": {
                    "tts": config.audio.tts.model_dump(
                        include={"engine", "voice", "split_on"}
                    ),
                    "stt": config.audio.stt.model_dump(include={"engine"}),
                },
                "file": config.rag.file.model_dump(),
                "permissions": config.user.permissions.model_dump(),
            }
            if user is not None
            else {}
        ),
    }
