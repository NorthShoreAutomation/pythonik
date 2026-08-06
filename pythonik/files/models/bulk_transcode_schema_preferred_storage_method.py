from enum import Enum


class BulkTranscodeSchemaPreferredStorageMethod(str, Enum):
    AZURE = "AZURE"
    B2 = "B2"
    CUSTOM = "CUSTOM"
    FILE = "FILE"
    FTP = "FTP"
    GCS = "GCS"
    HTTP = "HTTP"
    PORTAL = "PORTAL"
    S3 = "S3"
    SFTP = "SFTP"

    def __str__(self) -> str:
        return str(self.value)
