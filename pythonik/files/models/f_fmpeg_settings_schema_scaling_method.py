from enum import Enum


class FFmpegSettingsSchemaScalingMethod(str, Enum):
    ACCURATE_RND = "accurate_rnd"
    AREA = "area"
    BICUBIC = "bicubic"
    BICUBLIN = "bicublin"
    BILINEAR = "bilinear"
    BITEXACT = "bitexact"
    EXPERIMENTAL = "experimental"
    FAST_BILINEAR = "fast_bilinear"
    FULL_CHROMA_INP = "full_chroma_inp"
    FULL_CHROMA_INT = "full_chroma_int"
    GAUSS = "gauss"
    LANCZOS = "lanczos"
    NEIGHBOR = "neighbor"
    SINC = "sinc"
    SPLINE = "spline"

    def __str__(self) -> str:
        return str(self.value)
