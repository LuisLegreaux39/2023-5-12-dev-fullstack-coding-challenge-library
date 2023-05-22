import { FC } from 'react'

const Main: FC<any> = ({ children }) => {
    return (
        <div className="dark:bg-gray-900 h-screen  overflow-auto">
            <div className="container px-6 py-10 mx-auto pb-10">
                {children}
            </div>
        </div>
    )
}
export default Main