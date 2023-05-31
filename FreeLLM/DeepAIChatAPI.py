from .pyDeepAI import ChatCompletion
import asyncio

import requests
from langchain.llms.base import LLM
from typing import Optional, List, Mapping, Any
import pydantic
import os
from langchain import PromptTemplate, LLMChain
from time import sleep



class DeepAIChat(LLM):
    
    history_data: Optional[List] = []
    chatbot : Optional[ChatCompletion] = None

    
    @property
    def _llm_type(self) -> str:
        return "custom"

    async def call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        if stop is not None:
            pass
            #raise ValueError("stop kwargs are not permitted.")
        #cookie is a must check
        if self.chatbot == None:
            self.chatbot = ChatCompletion()
        #print(response)
        response_text = ""
        for chunk in self.chatbot.create(prompt):
            response_text += chunk
        #add to history
        self.history_data.append({"prompt":prompt,"response":response_text})    
        
        return response_text
    
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        return asyncio.run(self.call(prompt=prompt))

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"model": "BardCHAT", "cookie": self.cookie}



#llm = BardChat(cookie = "YOURCOOKIE") #for start new chat

#print(llm("Hello, how are you?"))
#print(llm("what is AI?"))
#print(llm("Can you resume your previus answer?")) #now memory work well
