import Post from './Post'
export default function Posts (props) {
    return (
        <div>
            {props.posts.map(post => (
                <Post 
                key={post.id} 
                id={post.id} 
                name={post.name} 
                remove__post={props.remove__post} />
            ))
            }
        </div>
    )
}