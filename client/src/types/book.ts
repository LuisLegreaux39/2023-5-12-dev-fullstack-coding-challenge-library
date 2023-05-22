import { z } from 'zod'

export const ZBookSchema = z.object({
    cover_image: z.string(),
    id: z.number().or(z.string()),
    name: z.string().min(1),
    description: z.string().min(1),
})

export type TBook = z.infer<typeof ZBookSchema>