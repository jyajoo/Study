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

function AccountLoginPage() {
  return (
    <MDBContainer fluid>
      <MDBRow className="d-flex justify-content-center align-items-center h-100">
        <MDBCol col="12">
          <MDBCard
            className="bg-white my-5 mx-auto"
            style={{ borderRadius: "1rem", maxWidth: "500px" }}
          >
            <MDBCardBody className="p-5 w-100 d-flex flex-column">
              <h2 className="fw-bold mb-2 text-center">로그인</h2>
              <p className="text-white-50 mb-3">
                Please enter your login and password!
              </p>

              <MDBInput
                wrapperClass="mb-4 w-100"
                label="아이디"
                id="formControlLg"
                type="text"
                size="lg"
              />
              <MDBInput
                wrapperClass="mb-4 w-100"
                label="비밀번호"
                id="formControlLg"
                type="password"
                size="lg"
              />
              <div className="mt-3 grid grid-flow-col auto-cols-fr gap-2 px-1">
                <input
                  className="btn btn-primary"
                  type="submit"
                  value="로그인"
                />
                <a href="/home/join" className="btn btn-secondary btn-outline">
                  가입하기
                </a>
              </div>
            </MDBCardBody>
          </MDBCard>
        </MDBCol>
      </MDBRow>
    </MDBContainer>
  );
}

export default AccountLoginPage;
