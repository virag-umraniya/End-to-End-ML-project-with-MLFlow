from mlProject import logger
from mlProject.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f">>> Stage {STAGE_NAME} started <<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>> Stage {STAGE_NAME} completed <<<\n\nx=============={STAGE_NAME}==================x")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>Stage {STAGE_NAME} started")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>Stage {STAGE_NAME} completed <<<<<\n\nx========{STAGE_NAME}=========x")
except Exception as e:
    logger.exception(e)
    raise e