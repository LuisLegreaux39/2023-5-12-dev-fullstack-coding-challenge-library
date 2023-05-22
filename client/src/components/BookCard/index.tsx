import { FC } from 'react'
import { TBook } from '../../types/book'
import { useNavigate } from 'react-router-dom'

const BookCard: FC<TBook> = ({ description, name, id, cover_image }) => {
  const navigate = useNavigate()
  return (
    <div className="flex flex-col items-center p-8 transition-colors duration-200 transform cursor-pointer group hover:bg-blue-600 rounded-xl" onClick={() => navigate(`/details/${id}`)}>
      <img
        className="object-cover w-32 h-35 ring-4 ring-gray-300"
        src={cover_image}
        alt=""
      />
      <h1 className="mt-4 text-2xl font-semibold text-gray-700 capitalize dark:text-white group-hover:text-white">
        {name}
      </h1>
      <p className="mt-2 text-gray-500 capitalize dark:text-gray-300 group-hover:text-gray-300">
        {description}
      </p>
    </div>

  )
}

export default BookCard