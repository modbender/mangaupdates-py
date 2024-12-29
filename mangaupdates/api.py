import client


def get_genres():
    mu_client = client.MangaUpdates()

    response = mu_client.session.get(mu_client.genre_url)
    response.raise_for_status()
    return response.json()


def get_categories():
    mu_client = client.MangaUpdates()

    categories = []
    page = 1

    while True:
        response = mu_client.session.post(
            mu_client.categories_url,
            json={
                "page": page,
                "perpage": 100,
            },
        )
        response.raise_for_status()
        data = response.json()
        results = data.get("results", [])

        if not results:
            break

        for result in results:
            record = result.get("record")
            category = record.get("category")
            categories.append(category)

        page += 1

    return categories
