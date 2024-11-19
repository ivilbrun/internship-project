Feature: User log in & User Guide

  Scenario: User can open User guide page
    Given open Reelly Sign In page
    When user logs in
    Then click on settings
    And click on User Guide option
    And verify the right page opens
    And verify all lesson videos contain titles

