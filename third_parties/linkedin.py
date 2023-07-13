import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from linkedin profiles.
    Manually scrape the information from the Linkedin profile"""

    ### Example with Linkedin ###
    ### PROXYCURL_API_KEY env config from https://nubela.co/proxycurl/dashboard/proxycurl-api/api-key/
    # api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    # header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    # response = requests.get(
    #     api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    # )

    ### Example from gist ###
    api_endpoint = "https://gist.githubusercontent.com/zilongqiu/da6f8e1837360c3160843ce76e6b52f2/raw/5a1402cac1220accf800c8ef79e184f13bdab950/gistfile1.json"
    response = requests.get(api_endpoint)

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
