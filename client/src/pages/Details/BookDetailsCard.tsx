import { FC } from 'react'
import axios from "axios";
import { useQuery } from "react-query";
import Loader from '../../components/Loader'
import BookDetails from '../../components/BookDetails';
import { TBook } from '../../types/book';

const BookDetailsCard: FC<{ book_id: TBook["id"] | string }> = ({ book_id }) => {

    const { isLoading, isError, data } = useQuery(["book"], () =>
        axios.get(`http://localhost:3002/api/book/${book_id}`).then((res) => res.data),
    );

    if (isLoading) return <Loader />;

    if (isError) return <>"An error has occurred: "</>;

    return <BookDetails {...data} />
}
export default BookDetailsCard