def is_remote(location, description):
    keywords = ["remote", "work from home", "distributed"]
    combined = f"{location} {description}".lower()
    return any(word in combined for word in keywords)


def requires_english(description):
    keywords = ["english", "fluent english", "written and verbal english"]
    return any(word in description.lower() for word in keywords)


def is_relevant_role(title, description):
    keywords = [
        "executive assistant",
        "admin assistant",
        "administrative support",
        "calendar management",
        "c-suite"
    ]
    combined = f"{title} {description}".lower()
    return any(word in combined for word in keywords)


def validate_job(job):
    return (
        is_remote(job["location"], job["description"]) and
        requires_english(job["description"]) and
        is_relevant_role(job["title"], job["description"])
    )
