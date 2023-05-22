
import { useQuery } from 'react-query';
import Loader from '../../components/Loader';
import Modal from '../../components/Modal'
import { FC } from 'react';
import { TBook } from '../../types/book';
import { TSection } from '../../types/section';
import PagesAccordion from '../PagesAccordion'
import { TPage } from '../../types/pages';
import fetcher from './../../services/axios';

const Pages: FC<{
    book_id: TBook["id"], section_id: TSection["id"]
} &
    Pick<TSection, "heading"> &
{ close?: () => void }

> = ({ book_id, section_id, heading, close }) => {

    const { isLoading, isError, data } = useQuery(["pages"], () =>
        fetcher.get(`/book/${book_id}/section/${section_id}/page`).then((res) => res.data),
    );
    if (isLoading) return <Loader />;

    if (isError) return <>"An error has occurred: "</>;
    return (
        <>
            <Modal >
                <>
                    {
                        data.map((item: TPage) => (<PagesAccordion {...item} section_name={heading} />))
                    }
                    <button
                        className="my-10 focus:outline-none focus:ring-2 focus:ring-offset-2  focus:ring-gray-400 ml-3 bg-gray-100 transition duration-150 text-gray-600 ease-in-out hover:border-gray-400 hover:bg-gray-300 border rounded px-8 py-2 text-sm"
                        onClick={() => close && close()}>
                        Cancel
                    </button>
                </>
            </Modal>
        </>
    )
}

export default Pages