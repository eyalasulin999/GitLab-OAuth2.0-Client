import httpx

APP_ID = "<>"
APP_SECRET = "gloas-<>"
APP_REDIRECT_URI = "<>"

GITLAB_AUTH_URL = "https://gitlab.com/oauth/authorize"
GITLAB_TOKEN_URL = "https://gitlab.com/oauth/token"


def generate_auth_url():
    params = {
        "client_id": APP_ID,
        "redirect_uri": APP_REDIRECT_URI,
        "response_type": "code"
    }
    return httpx.URL(GITLAB_AUTH_URL, params=params)


async def request_access_token(code):
    async with httpx.AsyncClient() as client:
        data = {
            "client_id": APP_ID,
            "client_secret": APP_SECRET,
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": APP_REDIRECT_URI,
        }
        res = await client.post(GITLAB_TOKEN_URL, data=data)
        res = res.json()
        return res if "access_token" in res else False


async def refresh_access_token(refresh_token):
    async with httpx.AsyncClient() as client:
        data = {
            "client_id": APP_ID,
            "client_secret": APP_SECRET,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
            "redirect_uri": APP_REDIRECT_URI,
        }
        res = await client.post(GITLAB_TOKEN_URL, data=data)
        res = res.json()
        return res if "access_token" in res else False
