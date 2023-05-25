import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import { NavLink } from "react-router-dom";

function Header() {
  return (
    <Navbar bg="primary" variant="dark">
      <Container>
        <Navbar.Brand href="/home/main">BOOTREPORT</Navbar.Brand>
        <Nav className="justify-text-end">
          <Nav.Link as={NavLink} to="/home/main" href="/home/main">
            HOME
          </Nav.Link>
          <Nav.Link as={NavLink} to="/account/login" href="/account/login">
            LOGIN
          </Nav.Link>
        </Nav>
      </Container>
    </Navbar>
  );
}

export default Header;
