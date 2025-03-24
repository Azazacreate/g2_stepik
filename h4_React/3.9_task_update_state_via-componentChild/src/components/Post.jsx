export default function Post (props) {
    const {id, name, remove__post} = props;
    return (
        <h2>
            {name}
            <button onClick={() => remove__post(id)}>
                delete
            </button>
        </h2>
    )
}