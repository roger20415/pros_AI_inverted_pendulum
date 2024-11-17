from rclpy.node import Node
from data_transformer import DataTransformer
from rl_training_pipeline.subscribe_data.data_subscriber import DataSubscriberNode
from subscribe_data.unity_data_store import UnityDataStore

class DataManager:
    def __init__(self) -> None:
        self.unity_data_store = UnityDataStore()
        self.data_transformer = DataTransformer(self.unity_data_store)
        self.data_subscriber = DataSubscriberNode(self.unity_data_store)
        
        return None
        
    def get_obervation(self) -> dict[str, float]:
        
        self.unity_data_store.turn_all_data_flag_to_unready()
        self.unity_data_store.wait_all_data_ready()
        self.observation_state: dict[str, float] = self.data_transformer.transform_untiy_data_to_state()
        
        return self.observation_state
    
    def get_data_subscriber_node(self) -> Node:
        return self.data_subscriber
            