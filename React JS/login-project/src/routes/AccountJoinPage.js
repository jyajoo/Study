import React from "react";
import {
  MDBContainer,
  MDBRow,
  MDBCol,
  MDBCard,
  MDBCardBody,
  MDBInput,
} from "mdb-react-ui-kit";
import "../css/AccountLoginPage.module.css";
import axios from "axios";

const CONFIG = {};
CONFIG.API_BASE = "http://localhost:8080";
CONFIG.API_JOIN = `${CONFIG.API_BASE}/member/join`;

function AccountJoinPage() {
  const onSubmit = async (event) => {
    event.preventDefault();

    const form = event.target;
    form.username.value = form.username.value.trim();
    form.password.value = form.password.value.trim();
    form.password2.value = form.password2.value.trim();

    if (form.username.value.length === 0) {
      alert("username을 입력해주세요.");
      form.username.focus();
      return;
    }

    if (form.password.value.length === 0) {
      alert("password를 입력해주세요.");
      form.password.focus();
      return;
    }

    if (form.password2.value.length === 0) {
      alert("비밀번호 재입력을 입력해주세요.");
      form.password.focus();
      return;
    }

    if (form.password.value.length !== form.password2.value.length) {
      alert("비밀번호가 서로 일치하지 않습니다.");
      form.password2.focus();
      return;
    }

    const username = form.username.value;
    const password = form.password.value;
    const password2 = form.password2.value;

    try {
      await axios.post(CONFIG.API_JOIN, {
        username,
        password,
        password2,
      });
    } catch (e) {
      console.error(e);
      form.password.focus();
    }
  };

  return (
    <MDBContainer fluid>
      <MDBRow className="d-flex justify-content-center align-items-center h-100">
        <MDBCol col="12">
          <MDBCard
            className="bg-white my-5 mx-auto"
            style={{ borderRadius: "1rem", maxWidth: "500px" }}
          >
            <MDBCardBody className="p-5 w-100 d-flex flex-column">
              <h2 className="fw-bold mb-2 text-center">회원 가입</h2>
              <p className="text-white-50 mb-3">
                Please enter your login and password!
              </p>
              <form onSubmit={onSubmit}>
                <MDBInput
                  wrapperClass="mb-4 w-100"
                  label="아이디"
                  id="formControlLg"
                  type="text"
                  size="lg"
                  name="username"
                />
                <MDBInput
                  wrapperClass="mb-4 w-100"
                  label="비밀번호"
                  id="formControlLg"
                  type="password"
                  size="lg"
                  name="password"
                />
                <MDBInput
                  wrapperClass="mb-4 w-100"
                  label="비밀번호 재입력"
                  id="formControlLg"
                  type="password"
                  size="lg"
                  name="password2"
                />
                <div className="mt-3 grid grid-flow-col auto-cols-fr gap-2 px-1">
                  <input
                    className="btn btn-primary"
                    type="submit"
                    value="가입하기"
                  />
                </div>
              </form>
            </MDBCardBody>
          </MDBCard>
        </MDBCol>
      </MDBRow>
    </MDBContainer>
  );
}

export default AccountJoinPage;
