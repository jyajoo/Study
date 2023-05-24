import { NavLink } from "react-router-dom";
import Nav from "react-bootstrap/Nav";

function Header() {
  return (
    // <ul className="flex shadow">
    //   <li>
    //     <Nav className="p-4 block" to="/home/main">
    //       홈
    //     </Nav>
    //   </li>
    //   <li>
    //     <NavLink className="p-4 block" to="/account/login">
    //       로그인
    //     </NavLink>
    //   </li>
    // </ul>
    <Nav className="justify-content-end" activeKey="/home/main">
      <Nav.Item>
        <Nav.Link href="/home/main">HOME</Nav.Link>
      </Nav.Item>
      <Nav.Item>
        <Nav.Link href="/account/login">LOGIN</Nav.Link>
      </Nav.Item>
    </Nav>
  );
}

export default Header;
