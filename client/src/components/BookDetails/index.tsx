import { FC } from 'react'
import { TBook } from '../../types/book'

const Index: FC<TBook> = ({ description, name, cover_image }) => {
    return (
        <section className="text-gray-600 body-font ">
            <div className="container px-1 py-5">
                <div className="p-10 dark:bg-gray-700 flex items-center mx-auto border-b rounded-lg sm:flex-row flex-col">
                    <div className="sm:w-32 sm:h-32 h-20 w-20 sm:mr-10 inline-flex items-center justify-center flex-shrink-0">
                        <img
                            className="object-cover w-32 h-35 ring-4 ring-gray-300"
                            src={cover_image}
                            alt=""
                        />
                    </div>
                    <div className="flex-grow sm:text-left text-center mt-6 sm:mt-0">
                        <h1 className="text-white text-2xl title-font font-bold mb-2">{name}</h1>
                        <p className="leading-relaxed text-white">{description}</p>
                    </div>
                </div>
            </div>
        </section>
    )
}

export default Index