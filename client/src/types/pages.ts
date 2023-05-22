import { z } from 'zod'

export const ZPageSchema = z.object({
    id: z.number().or(z.string()),
    content: z.string().min(1),
    section_id: z.number().or(z.string())

})

export type TPage = z.infer<typeof ZPageSchema>