from .pyChatBase import ChatBase
import asyncio

import requests
from langchain.llms.base import LLM
from typing import Optional, List, Mapping, Any
import pydantic
import os
from langchain import PromptTemplate, LLMChain
from time import sleep



class ChatBaseChat(LLM):
    
    history_data: Optional[List] = []
    chatbot : Optional[ChatBase] = None
    model: Optional[str] = "gpt-4"
    
    @property
    def _llm_type(self) -> str:
        return "custom"

    async def call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        if stop is not None:
            pass
            #raise ValueError("stop kwargs are not permitted.")
        if self.chatbot == None:
            self.chatbot = ChatBase()
               
        response = self.chatbot.GetAnswer(prompt, self.model)
        #print(response)
        #add to history
        self.history_data.append({"prompt":prompt,"response":response})    
        
        return response
    
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        return asyncio.run(self.call(prompt=prompt))

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"model": "CHATbase", "cookie": self.cookie}



#llm = BardChat(cookie = "YOURCOOKIE") #for start new chat

#print(llm("Hello, how are you?"))
#print(llm("what is AI?"))
#print(llm("Can you resume your previus answer?")) #now memory work well
