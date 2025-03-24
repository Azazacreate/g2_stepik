import React from 'react';
import '../styles/App.scss';
import burger from '../icons/1.1_burger.svg';
// import collab from '../icons/1.3.1_collab_offline.svg';
// import icon_search from '../icons/1.2.1_search.svg';
import man from '../icons/1.4_man.svg';
// import icon1 from '../icons/2.1.svg';
// import icon2 from '../icons/2.2.svg';
// import icon3 from '../icons/2.3.svg';
// import icon4 from '../icons/2.4.svg';
// import icon5 from '../icons/2.5.svg';
// import icon6 from '../icons/2.6.svg';
// import icon7 from '../icons/2.7.svg';
import { useEffect } from 'react';          // import useAside from './open__aside';


const Header = (props) => {
    useAside();
    return (
        <nav className='container1'>
            <div className="nav">
                <div className='nav_panel1'>
                    <button className="nav_button open__aside"><img src={burger} alt="burger" className='nav_panel1_icon' /></button>
                    {/* <button className="nav_button open__aside"><img src={icon_search} alt="search" className='nav_panel1_icon' /></button> */}
                    <input type="text" className='nav_panel1_input' placeholder='Корпорация МИТ' />
                    {/* <button className="nav_button open__aside"><img src={collab} alt="collab" className='nav_panel1_icon' /></button> */}
                    <button className="nav_button open__aside"><img src={man} alt="man" className='nav_panel1_icon' /></button>
                </div>
                <div className='nav_panel2'>
                    {/* <img src={icon1} alt="photo" className='nav_panel1_icon' />
                    <img src={icon2} alt="video" className='nav_panel1_icon' />
                    <img src={icon3} alt="screenshot" className='nav_panel1_icon' />
                    <img src={icon4} alt="record" className='nav_panel1_icon' />
                    <img src={icon5} alt="image" className='nav_panel1_icon' />
                    <img src={icon6} alt="picture" className='nav_panel1_icon' />
                    <img src={icon7} alt="file" className='nav_panel1_icon' /> */}
                    <a href="#"><div><p>для инвесторов</p></div></a>
                    <a href="#"><div><p>для партнеров</p></div></a>
                </div>
            </div>
        </nav>
    )
}
export default Header;


const useAside = () => {
    useEffect(() => {
        const btns = document.querySelectorAll('.open__aside'); // Change to querySelectorAll if you expect multiple buttons
        const aside = document.querySelector('.aside');
        const closeAside = aside.querySelector('.close__aside');

        if (!btns.length || !aside) return; // Avoid running further if elements were not found

        const openAside = () => {
            aside.classList.add('asideActive');
        };
        const closeAsideHandler = () => {
            aside.classList.remove('asideActive');
        };
        const hideAside = (event) => {
            if (event.target === aside) {
                closeAsideHandler();
            }
        };

        btns.forEach(btn => btn.onclick = openAside);
        closeAside.addEventListener('click', closeAsideHandler);
        aside.addEventListener('click', hideAside);

        // Cleanup event listeners on component unmount
        return () => {
            btns.forEach(btn => btn.onclick = null);
            closeAside.removeEventListener('click', closeAsideHandler);
            aside.removeEventListener('click', hideAside);
        };
    }, []);
};