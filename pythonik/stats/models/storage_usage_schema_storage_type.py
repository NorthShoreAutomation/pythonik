from enum import Enum


class StorageUsageSchemaStorageType(str, Enum):
    AZURE = "AZURE"
    B2 = "B2"
    FILE = "FILE"
    FTP = "FTP"
    GCS = "GCS"
    HTTP = "HTTP"
    OMMS = "OMMS"
    S3 = "S3"
    SFTP = "SFTP"
    TRANSFER = "TRANSFER"

    def __str__(self) -> str:
        return str(self.value)
