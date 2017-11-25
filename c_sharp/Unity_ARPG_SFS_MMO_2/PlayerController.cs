using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour {

    public float moveSpeed = 5;
	private float currentMoveSpeed;
    public float diagonalMoveModifier = 0.75f;

	private Animator anim;
	private Rigidbody2D myRigidbody;

	private bool playerMoving;
    public Vector2 lastMove = new Vector2(0, 0);

	private static bool playerExists;

    private bool attacking;
    public float attackTime = 0.35f;
	private float attackTimeCounter;

	public string startPoint;

    public bool canMove;

    // for interpolation
    public bool MovementDirty { get; set; }

	// Use this for initialization
	void Start () {
        MovementDirty = false;
        attacking = false;

		anim = GetComponent<Animator> ();
		myRigidbody = GetComponent<Rigidbody2D> ();

		if (!playerExists) {
			playerExists = true;
			// FOLLOW TO NEW SCENES
			DontDestroyOnLoad (transform.gameObject);

		} else {
			//Destroy (gameObject);
		}

        canMove = true;
	}
	
	// Update is called once per frame
	void Update () {

		playerMoving = false;

        //CURRENTLY STOPS MOVING FOR DIALOG BOXES
        if (!canMove)
        {
            myRigidbody.velocity = Vector2.zero;
            return;
        }

        //CAN MOVE AND ATTACK, BUT CANT MOVE WHILE ATTACKING
		if (!attacking) {

		    // MOVING ON THE X AXIS
		    if (Input.GetAxisRaw ("Horizontal") > 0.5f || Input.GetAxisRaw ("Horizontal") < -0.5f) {
			    //transform.Translate (new Vector3 (Input.GetAxisRaw ("Horizontal") * moveSpeed * Time.deltaTime, 0f, 0f));
			    myRigidbody.velocity = new Vector2 (Input.GetAxisRaw ("Horizontal") * currentMoveSpeed, myRigidbody.velocity.y);
			    playerMoving = true;
                MovementDirty = true;
			    lastMove = new Vector2 (Input.GetAxisRaw ("Horizontal"), 0f);
		    }

		    // MOVING ON THE Y AXIS
		    if (Input.GetAxisRaw ("Vertical") > 0.5f || Input.GetAxisRaw ("Vertical") < -0.5f) {
			    //transform.Translate (new Vector3 (0f, Input.GetAxisRaw ("Vertical") * moveSpeed * Time.deltaTime, 0f));
			    myRigidbody.velocity = new Vector2 (myRigidbody.velocity.x, Input.GetAxisRaw ("Vertical") * currentMoveSpeed);
			    playerMoving = true;
                MovementDirty = true;
			    lastMove = new Vector2 (0f, Input.GetAxisRaw ("Vertical"));
		    }
			
		    if (Input.GetAxisRaw ("Horizontal") < 0.5f && Input.GetAxisRaw ("Horizontal") > -0.5f) {
			    myRigidbody.velocity = new Vector2 (0f, myRigidbody.velocity.y);
		    }

		    if (Input.GetAxisRaw ("Vertical") < 0.5f && Input.GetAxisRaw ("Vertical") > -0.5f) {
			    myRigidbody.velocity = new Vector2 (myRigidbody.velocity.x, 0f);
		    }

            //ATTACK LINE
		    if (Input.GetKeyDown (KeyCode.Space)) {
			    attackTimeCounter = attackTime;
			    attacking = true;
			    myRigidbody.velocity = Vector2.zero;
			    anim.SetBool ("Attack", true);
		    }

            //SLOWING DOWN DIAGONAL MOVEMENT
		    if (Mathf.Abs (Input.GetAxisRaw ("Horizontal")) > 0.5f && Mathf.Abs (Input.GetAxisRaw ("Vertical")) > 0.5f) {
			    currentMoveSpeed = moveSpeed * diagonalMoveModifier;
		    } else 
		    {
			    currentMoveSpeed = moveSpeed;
		    }
		}

		if (attackTimeCounter > 0) 
		{
			attackTimeCounter -= Time.deltaTime;
		}

		if (attackTimeCounter < 0) 
		{
			attacking = false;
			anim.SetBool ("Attack", false);
		}

		anim.SetFloat ("MoveX", Input.GetAxisRaw ("Horizontal"));
		anim.SetFloat ("MoveY", Input.GetAxisRaw ("Vertical"));
		anim.SetBool ("PlayerMoving", playerMoving);
		anim.SetFloat ("LastMoveX", lastMove.x);
		anim.SetFloat ("LastMoveY", lastMove.y);

	
	}
}
