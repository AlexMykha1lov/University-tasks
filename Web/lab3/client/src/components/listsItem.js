import React from 'react';
import {Row, Col} from 'react-bootstrap';
import {useNavigate} from 'react-router-dom';

const ListsItem = ({listsItem}) => {
    const navigate = useNavigate();
    return (
        <Row>
            <Col  className='text-center border-bottom border-dark mb-4' onClick={() => navigate('/list/' + listsItem.id, {replace: true})}><h4>{listsItem.name}</h4></Col>
        </Row>
    );
}

export default ListsItem;