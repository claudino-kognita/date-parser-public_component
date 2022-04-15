IMAGE_NAME = "registry.gitlab.com/driyca/date-parser"
IMAGE_TAG = "v1.0.0"
DISPLAY_NAME = "Parse Datetime"
CONTAINER_NAME = "date_parser"

MEMORY_REQUEST = '10Mi'
MEMORY_LIMIT = '20Mi'
CPU_REQUEST = '100m'
CPU_LIMIT = '200m'

STARTUP_COMMAND = "date-parser"

OUTPUT_PATH = "output.txt"
