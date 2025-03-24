import React from 'react';
import '../styles/App.scss';
import icon_arrow from '../icons/icon_arrow.svg';
import icon_plus from '../icons/icon_plus.svg';

const template_page = () => {
    return (
        <div>
            <div className='row'>
                <button className='row_arrow'><img src={icon_arrow} alt="icon_arrow" /></button>
                <div className='row_name'><p>название</p></div>
                <button className='row_plus'><img src={icon_plus} alt="icon_plus" /></button>
            </div>
        </div>
    )
}
export default template_page;