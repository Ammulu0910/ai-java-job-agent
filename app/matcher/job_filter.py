JAVA_KEYWORDS = [
    "java",
    "spring",
    "spring boot",
    "backend",
    "microservices",
    "api",
    "software engineer",
    "platform engineer",
    "developer",
    "engineer"
]


def is_java_job(title):

    title = title.lower()

    for keyword in JAVA_KEYWORDS:

        if keyword in title:

            return True

    return False