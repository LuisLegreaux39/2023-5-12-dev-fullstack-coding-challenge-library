import { z } from 'zod'

export const ZSectionSchema = z.object({
    id: z.number().or(z.string()),
    heading: z.string().min(1),
    parent_section: z.string().min(1),
    book_id: z.number(),

})

export type TSection = z.infer<typeof ZSectionSchema>