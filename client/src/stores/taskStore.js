import { defineStore } from 'pinia'
import { ref } from 'vue'

import {api} from "@/api.js"
import {getCookie} from "../../composables/cookies.js";

export const useTaskStore = defineStore('task', () => {
  const taskID = ref(null)
  const taskResult = ref(null)

  const createTask = async (image) => {
    const formData = new FormData()
    formData.append('image', image)

    const response = await api.post('/search/', formData, {
      headers: {
        'X-CSRFToken': getCookie('csrftoken'),
      },
    })

    taskID.value = response.taskID

    return response

  }

  const checkTaskStatus = async () => {
    console.log(taskID.value)
    if (!taskID.value) return

    const response = await api.get(`/status/${taskID.value}/`)

    if (response.status === 'SUCCESS') {
      taskResult.value = response.result
    }

    return response
  }

  const clearStore = () => {
    taskID.value = null
    taskResult.value = null
  }

  return { taskResult, createTask, checkTaskStatus, clearStore }
})
