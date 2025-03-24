import React from 'react';
import '../styles/App.scss';
// import folder from '../icons/1.4_folder.svg';
import img_3 from '../imgs/img_3.jpg'

const Main = () => {
    return (
        <main className='container'>
            <aside className='aside'>
                <div className="aside_content">
                    <span className="close__aside">{/* &times; */}</span>
                    <ul>
                        <li><a href="1"><div>Private</div></a></li>
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
                    </ul>
                </div>
            </aside>
            <article className='article'>
                <h2 className='article_h2'>АО «Корпорация «Московский институт теплотехники»</h2>
                {/* <hr /> */}
                <br />
                <img src={img_3} alt="МИТ" />
                <textarea name="textarea" id="#" className='article_textarea'>Textarea</textarea>
            </article>
        </main>
    )
}
export default Main;