import BookDetailsCard from './BookDetailsCard';
import Sections from './Sections'

import { useParams } from 'react-router-dom'

const Details = () => {

    const { book_id } = useParams<{ book_id: string }>()

    if (!book_id) return null;
    return (
        <>
            <BookDetailsCard book_id={book_id} />
            <h1 className="text-3xl font-semibold text-center mb-10 text-gray-800 capitalize lg:text-4xl dark:text-white">Sections</h1>
            <Sections book_id={book_id} />
        </>
    )
}

export default Details