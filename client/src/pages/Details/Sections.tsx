import { FC } from 'react'
import { TSection } from '../../types/section'
import Loader from '../../components/Loader'
import { TBook } from '../../types/book'
import { useQuery } from 'react-query'
import fetcher from './../../services/axios';
import SectionOption from '../../components/SectionOption'

const Sections: FC<{ book_id: TBook["id"] }> = ({ book_id }) => {

    const { isLoading, isError, data } = useQuery(["sections"], () =>
        fetcher.get(`/book/${book_id}/section`).then((res) => res.data),
    );
    if (isLoading) return <Loader />;

    if (isError) return <>"An error has occurred: "</>;
    return (
        <>

            <ul role="list" className="divide-y divide-gray-100">
                {data.map((item: TSection) => (
                    <li key={item.id} className="flex justify-between rounded cursor-pointer mb-10 gap-x-6 py-5 dark:bg-gray-700 hover:bg-gray-500">
                        <SectionOption {...item} />
                    </li>
                ))}

            </ul>
        </>
    )
}

export default Sections