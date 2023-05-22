import Title from '../../components/Tittle'
import BookCard from '../../components/BookCard'
import Loader from '../../components/Loader'

import { useQuery } from "react-query";
import { TBook } from '../../types/book';
import fetcher from './../../services/axios';

const Home = () => {

    const { isLoading, isError, data } = useQuery(["books"], () =>
        fetcher.get("/book").then((res) => res.data)
    );

    if (isLoading) return <Loader />;

    if (isError) return <>"An error has occurred: "</>;

    return (
        <>
            <Title />
            <div className="grid grid-cols-1 gap-8 mt-8 xl:mt-16 md:grid-cols-2 xl:grid-cols-4">
                {data.map((item: TBook) => (<BookCard {...item} key={item.id} />))}
            </div>
        </>
    )
}

export default Home