import { FC, useState } from 'react'
import { TPage } from '../../types/pages'

const Index: FC<Pick<TPage, "content"> & { section_name: string }> = ({ content, section_name }) => {
    const [expand, setExpand] = useState<boolean>(false)
    return (
        <div id="accordion-flush" data-accordion="collapse"
            data-active-classNames="dark:bg-gray-900 text-gray-900 dark:text-white"
            data-inactive-classNames="text-gray-500 dark:text-gray-400">
            <h2 id="accordion-flush-heading-1">
                <button onClick={() => setExpand(!expand)} type="button" className="flex justify-between items-center py-5 w-full font-medium text-left text-gray-900 rounded-t-xl border-b border-gray-200 dark:border-gray-700 dark:text-white" data-accordion-target="#accordion-flush-body-1" aria-expanded="true" aria-controls="accordion-flush-body-1">
                    <span>{section_name}</span>
                    {expand ?
                        <svg data-accordion-icon className="w-6 h-6 rotate-180 shrink-0" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg> :
                        <svg data-accordion-icon className="w-6 h-6 shrink-0" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                    }

                </button>
            </h2>
            {expand && <div id="accordion-flush-body-1" aria-labelledby="accordion-flush-heading-1">
                <div className="py-5 border-b border-gray-200 dark:border-gray-700">
                    <p className="text-gray-500 dark:text-gray-400">
                        {content}
                    </p>
                </div>
            </div>}
        </div>
    )
}

export default Index