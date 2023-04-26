import { useMutation, useQuery, useQueryClient } from "react-query";


export default function Todos() {
  const queryClient = useQueryClient()

  const query = useQuery('todos', getTodos)

  const mutation = useMutation(postTodo, {
    onSuccess: () => {
      queryClient.invalidateQueries('todos')
    },
  })

  return (
    <div>
      <ul>
        {query.data.map(todo => (
          <li key={todo.id}>{todo.title}</li>
        ))} ;
      </ul>

      <button
        onClick={() => {
          mutation.mutate({
            id: Date.now(),
            title: 'Do Laundry',
          })
        }}
      >
        Add Todo
      </button>
    </div>
  )
}