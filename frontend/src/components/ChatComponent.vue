<template>
  <div class="flex flex-col h-screen bg-gray-100">
    <h2 class="text-2xl font-semibold text-center mb-4 p-4 bg-white shadow-md">Hackathon Idea Generator</h2>
    
    <!-- Chat box -->
    <div class="flex-1 overflow-y-auto p-4 space-y-4 bg-gray-50">
      <div v-for="(chat, index) in chats" :key="index" class="chat-message">

        <div v-if="chat.sender === 'user'" class="flex justify-end">
          <div class="max-w-[70%] sm:max-w-[60%] md:max-w-[50%] lg:max-w-[40%] bg-blue-100 p-3 rounded-md shadow-md">
            <div class="text-sm font-semibold text-blue-500">You:</div>
            <div>{{ chat.message }}</div>
          </div>
        </div>
        
        <div v-else-if="chat.sender === 'ai'" class="flex justify-start">
          <div class="max-w-[70%] sm:max-w-[60%] md:max-w-[50%] lg:max-w-[40%] bg-gray-200 p-3 rounded-md shadow-md">
            <div class="text-sm font-semibold text-green-500">AI:</div>
            <div>{{ chat.response }}</div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Input area with buttons aligned side by side -->
    <div class="flex items-center p-4 bg-white shadow-md space-x-4">
      <input
        v-model="message"
        class="flex-1 p-3 border border-gray-300 rounded-md"
        type="text"
        placeholder="Type your message"
        @keyup.enter="sendMessage"
      />
      <button 
        class="bg-blue-500 text-white p-3 rounded-md hover:bg-blue-600 focus:outline-none"
        @click="sendMessage"
      >
        Send
      </button>
      <button 
        class="bg-green-500 text-white p-3 rounded-md hover:bg-green-600 focus:outline-none"
        @click="fetchOldIdeas"
      >
        Fetch Old Ideas
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ChatComponent',
  data() {
    return {
      message: '', // User input
      chats: [], // Stores chat history
    };
  },
  methods: {
    async sendMessage() {
      if (!this.message.trim()) {
        alert('Please enter a message.');
        return;
      }

      try {
        // Send the message to the Django backend
        const response = await axios.post('http://127.0.0.1:8000/api/chat/', {
          message: this.message,
        });

        // Add the user's message to the chat history
        this.chats.push({
          message: this.message,
          sender: 'user', // Mark the sender as 'user'
        });

        // Add the AI's response to the chat history
        this.chats.push({
          response: response.data.response,
          sender: 'ai', // Mark the sender as 'ai'
        });

        // Clear the input field
        this.message = '';
      } catch (error) {
        console.error('Error communicating with the backend:', error);
        alert('Failed to send the message. Please try again later.');
      }
    },

    async fetchOldIdeas() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/hackathon-ideas/');
        response.data.forEach(idea => {
          this.chats.push({
            response: `Idea: ${idea.name}\nDescription: ${idea.description}\nBuild Approach: ${idea.build_approach}`,
            sender: 'ai',
          });
        });
      } catch (error) {
        console.error('Error fetching old ideas:', error);
        alert('Failed to fetch old ideas. Please try again later.');
      }
    }
  },
};
</script>
