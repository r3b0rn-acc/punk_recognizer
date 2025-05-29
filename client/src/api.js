import { mande } from 'mande'

export const api = mande('/api', {
  credentials: 'include',
})
