JAVA_KEYWORDS = {
    "java": 30,
    "spring": 25,
    "spring boot": 30,
    "backend": 20,
    "microservices": 20,
    "api": 15,
    "software engineer": 10,
    "developer": 10,
    "engineer": 5
}


def calculate_job_score(title):

    title = title.lower()

    score = 0

    for keyword, points in JAVA_KEYWORDS.items():

        if keyword in title:

            score += points

    return score


def is_java_job(title):

    score = calculate_job_score(title)

    return score >= 10