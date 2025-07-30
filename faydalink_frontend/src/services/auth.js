import { UserManager } from 'oidc-client';

const config = {
  authority: 'https://fayda-oidc.nationalid.gov.et',
  client_id: process.env.REACT_APP_FAYDA_CLIENT_ID,
  redirect_uri: window.location.origin + '/callback',
  response_type: 'code',
  scope: 'openid nationalid profile',
};

const userManager = new UserManager(config);

export function login() {
  userManager.signinRedirect();
}

export function logout() {
  userManager.signoutRedirect();
}

export async function handleCallback() {
  return await userManager.signinRedirectCallback();
}

export async function getUser() {
  return await userManager.getUser();
}
