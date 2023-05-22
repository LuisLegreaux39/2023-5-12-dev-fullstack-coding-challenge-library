import { FC } from 'react'

const Index: FC<any> = ({ children }) => {
    return (
        <div className="bg-slate-800 bg-opacity-50 flex justify-center  items-center absolute top-0 right-0 bottom-0 left-0">
            <div className="y-14 dark:bg-gray-900 w-1/2 h-3/4  px-16 p rounded-md text-center overflow-auto">
                {children}
            </div>
        </div>
    )
}

export default Index