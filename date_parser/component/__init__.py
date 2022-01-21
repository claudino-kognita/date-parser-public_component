from kfp import dsl
from kfp.dsl import ContainerOp

from date_parser.component.constants import IMAGE_NAME, IMAGE_TAG, MEMORY_LIMIT, CPU_LIMIT, CPU_REQUEST, \
    MEMORY_REQUEST, STARTUP_COMMAND, DISPLAY_NAME, CONTAINER_NAME, OUTPUT_PATH
from date_parser.component.utils import setup_resources


@dsl.component
def make_date_parser(datetime: str, input_format: str, output_format: str, days_to_add: int,
                     command: str = STARTUP_COMMAND, image_name: str = IMAGE_NAME, image_tag: str = IMAGE_TAG,
                     memory_limit: int = MEMORY_LIMIT, memory_request: int = MEMORY_REQUEST,
                     cpu_limit: int = CPU_LIMIT, cpu_request: int = CPU_REQUEST, display_name: str = DISPLAY_NAME,
                     ) -> ContainerOp:

    image = f"{image_name}:{image_tag}"

    operator = ContainerOp(
        name=CONTAINER_NAME,
        image=image,
        command=command,
        arguments=[
            "--input-format", input_format,
            "--output-format", output_format,
            "--save-to", OUTPUT_PATH,
            f"--add-days={days_to_add}",
            datetime
        ],
        file_outputs={
            'output': OUTPUT_PATH,
        }
    )

    operator = operator.set_display_name(display_name)
    operator = setup_resources(operator, memory_request, memory_limit, cpu_request, cpu_limit)

    return operator


