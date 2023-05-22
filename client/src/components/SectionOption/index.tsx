import { FC, useState } from 'react'
import { TSection } from '../../types/section'
import PagesModal from '../PagesModal'

const Index: FC<TSection> = ({ heading, parent_section, id, book_id }) => {

    const [showPages, setShowPages] = useState<boolean>(false);

    return (
        <div className="flex gap-x-4 w-full justify-around" onClick={() => setShowPages(true)} >
            {showPages && <PagesModal book_id={book_id} section_id={id} heading={heading} close={() => setShowPages(false)} />}
            <div className="min-w-10 mx-12 flex-auto text-white">
                <p className="text-m font-semibold leading-6 ">{heading}</p>
                <p className="mt-1 truncate text-xs leading-5">{parent_section}</p>
            </div>
            <div className="min-w-10 mx-12 flex-end text-white">
                <button className="group rounded-2xl h-12 w-48 dark:bg-gray-800 font-bold text-lg text-white relative overflow-hidden">
                    Show Pages
                </button>
            </div>
        </div>
    )
}

export default Index