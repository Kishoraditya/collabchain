// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DataAgreementContract {
    struct Agreement {
        uint id;
        address proposer;
        address acceptor;
        string terms;
        bool isAccepted;
        uint timestamp;
    }

    uint public agreementCount = 0;
    mapping(uint => Agreement) public agreements;

    function proposeAgreement(address _acceptor, string memory _terms) public {
        agreementCount++;
        agreements[agreementCount] = Agreement(agreementCount, msg.sender, _acceptor, _terms, false, block.timestamp);
    }

    function acceptAgreement(uint _id) public {
        Agreement storage agreement = agreements[_id];
        require(msg.sender == agreement.acceptor, "Not authorized");
        agreement.isAccepted = true;
    }

    function getAgreement(uint _id) public view returns (Agreement memory) {
        return agreements[_id];
    }
}
