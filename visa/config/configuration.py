import os,sys
from visa.constant import *
from visa.logger import logging
from visa.exception import CustomException
from visa.entity.config_entity import *
from visa.utils.utils import read_yaml_file #helper function

class Configuration:

    def __init__(self,
                 config_file_path:str=CONFIG_FILE_PATH,
                 current_time_stamp:str = CURRENT_TIME_STAMP
                 ) -> None:
       
        try:
            self.config_info = read_yaml_file(file_path=config_file_path)
            self.time_stamp = current_time_stamp
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp
        except Exception as e:
            raise CustomException(e,sys) from e
        


        def get_data_ingestion_config(self) ->DataIngestionConfig:
            try:
                
                artifact_dir = self.training_pipeline_config.artifact_dir
                data_ingestion_artifact_dir = os.path.join(
                    artifact_dir,
                    DATA_INGESTION_ARTIFACT_DIR,
                    self.time_stamp
                )

                data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]
                dataset_download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]

                raw_data_dir = os.path.join(data_ingestion_artifact_dir,
                                            data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY])
                
                ingested_data_dir = os.path.join(
                    data_ingestion_artifact_dir,
                    data_ingestion_info[DATA_INGESTION_INGESTED_DIR_KEY]
                )
                
                ingested_train_dir = os.path.join(
                    ingested_data_dir,
                    data_ingestion_info[DATA_INGESTION_INGESTED_TRAIN_DIR_KEY]
                )

                ingested_test_dir = os.path.join(
                    ingested_data_dir,
                    data_ingestion_info[DATA_INGESTION_INGESTED_TEST_DIR_KEY]
                )

                data_ingestion_config = DataIngestionConfig(
                    dataset_download_url = dataset_download_url,
                    raw_data_dir = raw_data_dir,
                    ingested_train_dir = ingested_train_dir,
                    ingested_test_dir= ingested_test_dir
                )

                logging.info(f"Data Ingestion config : {data_ingestion_config}")
                return data_ingestion_config

            except Exception as e:
                raise CustomException(e,sys) from e



    
