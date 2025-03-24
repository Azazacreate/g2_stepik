import React from 'react';
import '../styles/App.scss';
import Template_page from '../components/Template_page'

const Main = () => {
    return (
        <main className='container'>
            <aside className='aside'>
                <div className="aside_content">
                    <span className="close__aside">{/* &times; */}</span>
                    {/* <ul>
                        <li className='aside_li'><a href="1"><div>Private</div></a></li>
                        <li><a href="2"><div>unsorted</div></a></li>
                        <li>self-education</li>
                        <li>university</li>
                        <li>work</li>
                        <hr />
                        <li>Public</li>
                        <li>project-1</li>
                        <li>project-2</li>
                        <li>project-3</li>
                        <li>project-4</li>
                    </ul> */}
                    
                    <Template_page />
                    <Template_page />
                    <Template_page />
                    <Template_page />
                    <hr />
                    <Template_page />
                    <Template_page />
                    <Template_page />
                    <Template_page />
                </div>
            </aside>
            <article className='article'>
                <h2 className='article_h2'>Self-education</h2>
                <hr />
                <textarea name="textarea" id="#" className='article_textarea'>Textarea</textarea>
            </article>
        </main>
    )
}
export default Main;