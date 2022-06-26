import React from 'react';
import {Navbar, Container, Nav, Button} from "react-bootstrap";
import {NavLink} from "react-router-dom";
import {useNavigate} from 'react-router-dom';

const NavBar = () => {
    const navigate = useNavigate();
    return (
        <Navbar bg='dark'>
            <Container>
            <Navbar.Brand style={{color: 'white'}}>Memento</Navbar.Brand>
            <Nav>
                <Button className="ms-4" onClick={() => navigate('/', {replace: true})}>Lists</Button>
            </Nav>
            </Container>
        </Navbar>
    )
};

export default NavBar;