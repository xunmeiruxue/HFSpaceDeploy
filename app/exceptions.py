
class SpaceDeployError(Exception):
    """Base for deployment‑related faults."""

class RepoCloneError(SpaceDeployError):
    pass

class DockerfileMissingError(SpaceDeployError):
    pass

class SpaceCreationError(SpaceDeployError):
    pass

class SpaceBuildTimeoutError(SpaceDeployError):
    pass

class SpaceAlreadyExistsError(SpaceDeployError):
    pass