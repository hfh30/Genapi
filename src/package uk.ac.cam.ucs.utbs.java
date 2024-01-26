package uk.ac.cam.ucs.utbs.client;

import java.io.IOException;

import javax.xml.bind.JAXBException;

import uk.ac.cam.ucs.utbs.dto.UTBSResult;

public interface ClientConnection
{public enum Method {GET}

/**
 * Set the username to use when connecting to the UTBS web service. By
 * default connections are anonymous, which gives read-only access to a
 * limited set of data. Certain API methods, however, require
 * authentication as a user with elevated privileges, using the person's
 * API password.
 * <p>
 * This method may be called at any time, and affects all subsequent
 * access using this connection, but should not affect any other
 * ClientConnection objects.
 *
 * @param username The CRSid of the user to connect as.
 */
public void setUsername(String  username);

/**
 * Set the password to use when connecting to the UTBS web service. This
 * is only necessary when authenticating using
 * {@link #setUsername(String) setUserName()}, in which case the password
 * should be the user's API password.
 *
 * @param password The API password of the user.
 */
public void setPassword(String  password);

/**
 * Invoke a web service GET method.
 * <p>
 * The path should be the relative path to the method with standard
 * Java format specifiers for any path parameters, for example
 * {@code "api/v1/method/%1$s/%2$s"}. Any path parameters specified
 * are then substituted into the path according to the standard Java
 * formatting rules.
 *
 * @param path The path to the method to invoke.
 * @param pathParams Any path parameters that should be inserted into
 * the path in place of any format specifiers.
 * @param queryParams Any query parameters to add as part of the URL's
 * query string. These are expected to come in pairs {name1, value1,
 * name2, value2, ...}.
 * @return The result of invoking the method.
 */
public UTBSResult invokeMethod(String   path,
                               String[] pathParams,
                               Object[] queryParams)
    throws IOException, JAXBException;

/**
 * Invoke a web service GET, POST, PUT or DELETE method.
 * <p>
 * The path should be the relative path to the method with standard
 * Java format specifiers for any path parameters, for example
 * {@code "api/v1/method/%1$s/%2$s"}. Any path parameters specified
 * are then substituted into the path according to the standard Java
 * formatting rules.
 *
 * @param method The method type (GET, POST, PUT or DELETE).
 * @param path The path to the method to invoke.
 * @param pathParams Any path parameters that should be inserted into
 * the path in place of any format specifiers.
 * @param queryParams Any query parameters to add as part of the URL's
 * query string. These are expected to come in pairs {name1, value1,
 * name2, value2, ...}.
 * @param formParams Any form parameters to submit. These are expected
 * to come in pairs {name1, value1, name2, value2, ...}.
 * @return The result of invoking the method.
 */
public UTBSResult invokeMethod(Method   method,
                               String   path,
                               String[] pathParams,
                               Object[] queryParams,
                               Object[] formParams)
    throws IOException, JAXBException;
}
